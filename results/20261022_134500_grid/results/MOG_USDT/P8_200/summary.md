# EMA Hourly Continuation — MOG/USDT P8_200

**Symbol:** MOG/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.9033 |
| net_win_rate | 0.5189 |
| gross_profit_factor | 1.0917 |
| gross_win_rate | 0.5227 |
| sharpe_ratio | -0.4967 |
| sortino_ratio | -0.1209 |
| max_drawdown | 0.1836 |
| cagr | -0.0576 |
| net_avg_win | 86.8184 |
| net_avg_loss | -103.6804 |
| avg_hold_time_bars | 64.2311 |
| exposure | 0.8430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
