# EMA Hourly Continuation — TRB/USDT P12_89

**Symbol:** TRB/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 764 |
| net_profit_factor | 0.5543 |
| net_win_rate | 0.4424 |
| gross_profit_factor | 0.8535 |
| gross_win_rate | 0.4568 |
| sharpe_ratio | -5.4264 |
| sortino_ratio | -2.1074 |
| max_drawdown | 0.9222 |
| cagr | -0.6341 |
| net_avg_win | 33.8862 |
| net_avg_loss | -48.5015 |
| avg_hold_time_bars | 15.2971 |
| exposure | 0.5288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
