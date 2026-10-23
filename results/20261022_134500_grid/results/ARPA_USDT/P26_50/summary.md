# EMA Hourly Continuation — ARPA/USDT P26_50

**Symbol:** ARPA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1000 |
| net_profit_factor | 0.4643 |
| net_win_rate | 0.4220 |
| gross_profit_factor | 0.9107 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -8.8684 |
| sortino_ratio | -3.9798 |
| max_drawdown | 0.9931 |
| cagr | -0.8580 |
| net_avg_win | 20.3892 |
| net_avg_loss | -32.0615 |
| avg_hold_time_bars | 4.4680 |
| exposure | 0.2022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
