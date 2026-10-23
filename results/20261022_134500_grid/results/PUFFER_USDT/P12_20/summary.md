# EMA Hourly Continuation — PUFFER/USDT P12_20

**Symbol:** PUFFER/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1061 |
| net_profit_factor | 0.4414 |
| net_win_rate | 0.4251 |
| gross_profit_factor | 0.8251 |
| gross_win_rate | 0.4420 |
| sharpe_ratio | -10.3695 |
| sortino_ratio | -5.3058 |
| max_drawdown | 0.9956 |
| cagr | -0.9315 |
| net_avg_win | 17.4394 |
| net_avg_loss | -29.2136 |
| avg_hold_time_bars | 2.9698 |
| exposure | 0.1783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
