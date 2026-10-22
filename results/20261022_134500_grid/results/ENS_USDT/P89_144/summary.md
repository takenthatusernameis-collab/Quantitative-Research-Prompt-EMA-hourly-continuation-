# EMA Hourly Continuation — ENS/USDT P89_144

**Symbol:** ENS/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.3872 |
| net_win_rate | 0.4128 |
| gross_profit_factor | 0.6980 |
| gross_win_rate | 0.4264 |
| sharpe_ratio | -6.2568 |
| sortino_ratio | -1.9963 |
| max_drawdown | 0.9220 |
| cagr | -0.6332 |
| net_avg_win | 27.2714 |
| net_avg_loss | -49.5146 |
| avg_hold_time_bars | 4.9322 |
| exposure | 0.1157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
