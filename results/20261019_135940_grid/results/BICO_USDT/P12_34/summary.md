# EMA Hourly Continuation — BICO/USDT P12_34

**Symbol:** BICO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1180 |
| net_profit_factor | 0.4758 |
| net_win_rate | 0.4483 |
| gross_profit_factor | 0.8684 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -7.2929 |
| sortino_ratio | -3.5305 |
| max_drawdown | 0.9861 |
| cagr | -0.8169 |
| net_avg_win | 16.9199 |
| net_avg_loss | -28.8939 |
| avg_hold_time_bars | 4.7958 |
| exposure | 0.2572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
