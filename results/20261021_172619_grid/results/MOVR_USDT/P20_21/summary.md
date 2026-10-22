# EMA Hourly Continuation — MOVR/USDT P20_21

**Symbol:** MOVR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 208 |
| net_profit_factor | 0.5759 |
| net_win_rate | 0.4567 |
| gross_profit_factor | 0.8259 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -2.4026 |
| sortino_ratio | -0.4956 |
| max_drawdown | 0.4732 |
| cagr | -0.2036 |
| net_avg_win | 62.2203 |
| net_avg_loss | -90.8378 |
| avg_hold_time_bars | 4.8125 |
| exposure | 0.0455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
