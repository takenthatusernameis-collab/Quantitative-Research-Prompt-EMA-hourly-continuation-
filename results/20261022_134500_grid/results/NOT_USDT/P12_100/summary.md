# EMA Hourly Continuation — NOT/USDT P12_100

**Symbol:** NOT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.6147 |
| net_win_rate | 0.4722 |
| gross_profit_factor | 0.9146 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -4.2157 |
| sortino_ratio | -1.5245 |
| max_drawdown | 0.8417 |
| cagr | -0.5254 |
| net_avg_win | 43.6200 |
| net_avg_loss | -63.4883 |
| avg_hold_time_bars | 19.1944 |
| exposure | 0.5843 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
