# EMA Hourly Continuation — LISTA/USDT P21_100

**Symbol:** LISTA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.8067 |
| net_win_rate | 0.4906 |
| gross_profit_factor | 0.9709 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -1.4922 |
| sortino_ratio | -0.4548 |
| max_drawdown | 0.4017 |
| cagr | -0.1903 |
| net_avg_win | 78.0788 |
| net_avg_loss | -93.2031 |
| avg_hold_time_bars | 20.6910 |
| exposure | 0.4290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
