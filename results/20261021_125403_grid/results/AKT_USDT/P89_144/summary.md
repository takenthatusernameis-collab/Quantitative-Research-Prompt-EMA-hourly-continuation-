# EMA Hourly Continuation — AKT/USDT P89_144

**Symbol:** AKT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.9623 |
| net_win_rate | 0.5530 |
| gross_profit_factor | 1.2337 |
| gross_win_rate | 0.5530 |
| sharpe_ratio | -0.1816 |
| sortino_ratio | -0.0429 |
| max_drawdown | 0.2874 |
| cagr | -0.0236 |
| net_avg_win | 101.8468 |
| net_avg_loss | -130.9566 |
| avg_hold_time_bars | 7.5189 |
| exposure | 0.0902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
