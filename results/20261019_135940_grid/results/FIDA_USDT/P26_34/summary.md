# EMA Hourly Continuation — FIDA/USDT P26_34

**Symbol:** FIDA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1040 |
| net_profit_factor | 0.3401 |
| net_win_rate | 0.4067 |
| gross_profit_factor | 0.9151 |
| gross_win_rate | 0.4548 |
| sharpe_ratio | -10.6439 |
| sortino_ratio | -4.8934 |
| max_drawdown | 0.9981 |
| cagr | -0.9162 |
| net_avg_win | 12.1626 |
| net_avg_loss | -24.5147 |
| avg_hold_time_bars | 2.7163 |
| exposure | 0.1278 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
