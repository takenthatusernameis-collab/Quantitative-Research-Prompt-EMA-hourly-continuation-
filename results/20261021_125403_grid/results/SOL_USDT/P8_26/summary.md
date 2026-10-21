# EMA Hourly Continuation — SOL/USDT P8_26

**Symbol:** SOL/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.8219 |
| net_win_rate | 0.5360 |
| gross_profit_factor | 1.1531 |
| gross_win_rate | 0.5360 |
| sharpe_ratio | -1.5906 |
| sortino_ratio | -0.5621 |
| max_drawdown | 0.5197 |
| cagr | -0.2276 |
| net_avg_win | 68.8158 |
| net_avg_loss | -96.7278 |
| avg_hold_time_bars | 6.7236 |
| exposure | 0.1825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
