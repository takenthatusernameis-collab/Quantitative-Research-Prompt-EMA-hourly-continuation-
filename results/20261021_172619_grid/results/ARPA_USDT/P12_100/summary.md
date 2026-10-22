# EMA Hourly Continuation — ARPA/USDT P12_100

**Symbol:** ARPA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.6938 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9027 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -2.8204 |
| sortino_ratio | -0.9923 |
| max_drawdown | 0.6942 |
| cagr | -0.3652 |
| net_avg_win | 52.9414 |
| net_avg_loss | -69.6301 |
| avg_hold_time_bars | 18.6650 |
| exposure | 0.5169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
