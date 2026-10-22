# EMA Hourly Continuation — JST/USDT P8_89

**Symbol:** JST/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.5021 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9881 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -4.4847 |
| sortino_ratio | -1.4983 |
| max_drawdown | 0.8580 |
| cagr | -0.5280 |
| net_avg_win | 30.6019 |
| net_avg_loss | -57.2612 |
| avg_hold_time_bars | 25.6332 |
| exposure | 0.6704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
