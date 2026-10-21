# EMA Hourly Continuation — IMX/USDT P50_89

**Symbol:** IMX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.8543 |
| net_win_rate | 0.5324 |
| gross_profit_factor | 1.1256 |
| gross_win_rate | 0.5324 |
| sharpe_ratio | -0.8811 |
| sortino_ratio | -0.2444 |
| max_drawdown | 0.2764 |
| cagr | -0.1079 |
| net_avg_win | 74.4732 |
| net_avg_loss | -99.2733 |
| avg_hold_time_bars | 6.1351 |
| exposure | 0.1027 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
