# EMA Hourly Continuation — ONE/USDT P50_100

**Symbol:** ONE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.6313 |
| net_win_rate | 0.4724 |
| gross_profit_factor | 1.0238 |
| gross_win_rate | 0.4818 |
| sharpe_ratio | -4.5595 |
| sortino_ratio | -1.6148 |
| max_drawdown | 0.8650 |
| cagr | -0.5425 |
| net_avg_win | 49.2257 |
| net_avg_loss | -69.8064 |
| avg_hold_time_bars | 5.9384 |
| exposure | 0.1709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
