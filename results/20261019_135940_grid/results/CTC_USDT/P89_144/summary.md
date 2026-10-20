# EMA Hourly Continuation — CTC/USDT P89_144

**Symbol:** CTC/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.4239 |
| net_win_rate | 0.4316 |
| gross_profit_factor | 0.8808 |
| gross_win_rate | 0.4563 |
| sharpe_ratio | -6.3830 |
| sortino_ratio | -2.0528 |
| max_drawdown | 0.9309 |
| cagr | -0.6512 |
| net_avg_win | 30.1098 |
| net_avg_loss | -53.9301 |
| avg_hold_time_bars | 4.8555 |
| exposure | 0.1161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
