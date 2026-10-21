# EMA Hourly Continuation — MINA/USDT P20_34

**Symbol:** MINA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.7127 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 1.0451 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -2.4719 |
| sortino_ratio | -0.7439 |
| max_drawdown | 0.6219 |
| cagr | -0.2890 |
| net_avg_win | 64.5779 |
| net_avg_loss | -91.8588 |
| avg_hold_time_bars | 5.4465 |
| exposure | 0.1087 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
