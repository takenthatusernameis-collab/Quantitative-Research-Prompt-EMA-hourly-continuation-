# EMA Hourly Continuation — JASMY/USDT P12_144

**Symbol:** JASMY/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.8051 |
| net_win_rate | 0.5310 |
| gross_profit_factor | 1.1278 |
| gross_win_rate | 0.5356 |
| sharpe_ratio | -1.3259 |
| sortino_ratio | -0.3875 |
| max_drawdown | 0.4238 |
| cagr | -0.1737 |
| net_avg_win | 68.0854 |
| net_avg_loss | -95.7567 |
| avg_hold_time_bars | 35.8161 |
| exposure | 0.7082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
