# EMA Hourly Continuation — AVA/USDT P21_144

**Symbol:** AVA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.8456 |
| net_win_rate | 0.5176 |
| gross_profit_factor | 1.0449 |
| gross_win_rate | 0.5176 |
| sharpe_ratio | -0.9228 |
| sortino_ratio | -0.2742 |
| max_drawdown | 0.4028 |
| cagr | -0.1211 |
| net_avg_win | 68.6336 |
| net_avg_loss | -87.0749 |
| avg_hold_time_bars | 23.9977 |
| exposure | 0.4658 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
