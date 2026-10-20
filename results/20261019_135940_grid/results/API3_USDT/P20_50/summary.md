# EMA Hourly Continuation — API3/USDT P20_50

**Symbol:** API3/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1035 |
| net_profit_factor | 0.5693 |
| net_win_rate | 0.4502 |
| gross_profit_factor | 0.9670 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -6.9097 |
| sortino_ratio | -3.1417 |
| max_drawdown | 0.9783 |
| cagr | -0.7793 |
| net_avg_win | 27.7255 |
| net_avg_loss | -39.8858 |
| avg_hold_time_bars | 4.8145 |
| exposure | 0.2265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
