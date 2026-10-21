# EMA Hourly Continuation — TFUEL/USDT P89_144

**Symbol:** TFUEL/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.5875 |
| net_win_rate | 0.4486 |
| gross_profit_factor | 0.8368 |
| gross_win_rate | 0.4486 |
| sharpe_ratio | -3.1963 |
| sortino_ratio | -0.8146 |
| max_drawdown | 0.6116 |
| cagr | -0.3120 |
| net_avg_win | 60.3984 |
| net_avg_loss | -83.6436 |
| avg_hold_time_bars | 7.1308 |
| exposure | 0.1036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
