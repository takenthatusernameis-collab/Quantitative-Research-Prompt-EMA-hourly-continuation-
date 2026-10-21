# EMA Hourly Continuation — ADA/USDT P8_144

**Symbol:** ADA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.8693 |
| net_win_rate | 0.5169 |
| gross_profit_factor | 1.0495 |
| gross_win_rate | 0.5169 |
| sharpe_ratio | -0.7180 |
| sortino_ratio | -0.1858 |
| max_drawdown | 0.2878 |
| cagr | -0.0843 |
| net_avg_win | 78.5436 |
| net_avg_loss | -96.6877 |
| avg_hold_time_bars | 49.9600 |
| exposure | 0.7380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
