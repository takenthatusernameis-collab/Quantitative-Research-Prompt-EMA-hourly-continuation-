# EMA Hourly Continuation — ILV/USDT P20_144

**Symbol:** ILV/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.8735 |
| net_win_rate | 0.5165 |
| gross_profit_factor | 1.0657 |
| gross_win_rate | 0.5165 |
| sharpe_ratio | -0.8554 |
| sortino_ratio | -0.2533 |
| max_drawdown | 0.2901 |
| cagr | -0.1128 |
| net_avg_win | 81.8520 |
| net_avg_loss | -100.1076 |
| avg_hold_time_bars | 27.3962 |
| exposure | 0.5280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
