# EMA Hourly Continuation — LUNA/USDT P12_34

**Symbol:** LUNA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.6713 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.9063 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -3.2739 |
| sortino_ratio | -1.0652 |
| max_drawdown | 0.7097 |
| cagr | -0.3867 |
| net_avg_win | 60.1764 |
| net_avg_loss | -76.8315 |
| avg_hold_time_bars | 6.6038 |
| exposure | 0.1561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
