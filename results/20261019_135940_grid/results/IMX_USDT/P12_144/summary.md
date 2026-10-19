# EMA Hourly Continuation — IMX/USDT P12_144

**Symbol:** IMX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.7097 |
| net_win_rate | 0.4893 |
| gross_profit_factor | 0.9326 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -2.1139 |
| sortino_ratio | -0.6452 |
| max_drawdown | 0.5513 |
| cagr | -0.2614 |
| net_avg_win | 57.2773 |
| net_avg_loss | -77.3202 |
| avg_hold_time_bars | 32.2597 |
| exposure | 0.6803 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
