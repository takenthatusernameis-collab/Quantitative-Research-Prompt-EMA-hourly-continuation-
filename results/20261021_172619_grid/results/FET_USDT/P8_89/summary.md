# EMA Hourly Continuation — FET/USDT P8_89

**Symbol:** FET/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.9696 |
| net_win_rate | 0.5312 |
| gross_profit_factor | 1.1195 |
| gross_win_rate | 0.5312 |
| sharpe_ratio | -0.1537 |
| sortino_ratio | -0.0486 |
| max_drawdown | 0.1922 |
| cagr | -0.0303 |
| net_avg_win | 92.9977 |
| net_avg_loss | -108.7018 |
| avg_hold_time_bars | 28.9021 |
| exposure | 0.6306 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
