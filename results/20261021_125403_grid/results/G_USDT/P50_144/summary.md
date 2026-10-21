# EMA Hourly Continuation — G/USDT P50_144

**Symbol:** G/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.6995 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 0.9126 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -1.9844 |
| sortino_ratio | -0.5286 |
| max_drawdown | 0.4556 |
| cagr | -0.2153 |
| net_avg_win | 65.7129 |
| net_avg_loss | -87.3171 |
| avg_hold_time_bars | 18.0199 |
| exposure | 0.2852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
