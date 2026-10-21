# EMA Hourly Continuation — NEAR/USDT P12_26

**Symbol:** NEAR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.7690 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0168 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -1.7275 |
| sortino_ratio | -0.5104 |
| max_drawdown | 0.4638 |
| cagr | -0.2089 |
| net_avg_win | 69.5153 |
| net_avg_loss | -91.6926 |
| avg_hold_time_bars | 5.1844 |
| exposure | 0.0997 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
