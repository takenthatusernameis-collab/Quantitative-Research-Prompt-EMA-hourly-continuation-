# EMA Hourly Continuation — AKT/USDT P8_144

**Symbol:** AKT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 548 |
| net_profit_factor | 0.6733 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 0.9602 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -2.8691 |
| sortino_ratio | -0.9353 |
| max_drawdown | 0.6937 |
| cagr | -0.3684 |
| net_avg_win | 52.8563 |
| net_avg_loss | -74.5873 |
| avg_hold_time_bars | 28.3011 |
| exposure | 0.7050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
