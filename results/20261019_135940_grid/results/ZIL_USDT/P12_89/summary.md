# EMA Hourly Continuation — ZIL/USDT P12_89

**Symbol:** ZIL/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 742 |
| net_profit_factor | 0.5737 |
| net_win_rate | 0.4623 |
| gross_profit_factor | 0.9341 |
| gross_win_rate | 0.4730 |
| sharpe_ratio | -5.1675 |
| sortino_ratio | -1.9615 |
| max_drawdown | 0.9201 |
| cagr | -0.6214 |
| net_avg_win | 35.8163 |
| net_avg_loss | -53.6665 |
| avg_hold_time_bars | 15.6739 |
| exposure | 0.5286 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
