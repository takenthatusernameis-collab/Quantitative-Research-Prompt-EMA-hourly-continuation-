# EMA Hourly Continuation — XPR/USDT P89_200

**Symbol:** XPR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.8635 |
| net_win_rate | 0.5330 |
| gross_profit_factor | 1.1173 |
| gross_win_rate | 0.5330 |
| sharpe_ratio | -0.5929 |
| sortino_ratio | -0.1291 |
| max_drawdown | 0.2135 |
| cagr | -0.0589 |
| net_avg_win | 73.9615 |
| net_avg_loss | -97.7705 |
| avg_hold_time_bars | 16.3656 |
| exposure | 0.1689 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
