# EMA Hourly Continuation — SUPER/USDT P12_200

**Symbol:** SUPER/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.9452 |
| net_win_rate | 0.5250 |
| gross_profit_factor | 1.0892 |
| gross_win_rate | 0.5250 |
| sharpe_ratio | -0.2570 |
| sortino_ratio | -0.0617 |
| max_drawdown | 0.2242 |
| cagr | -0.0323 |
| net_avg_win | 92.7994 |
| net_avg_loss | -108.5194 |
| avg_hold_time_bars | 58.9036 |
| exposure | 0.7497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
