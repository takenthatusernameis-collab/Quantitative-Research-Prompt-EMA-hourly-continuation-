# EMA Hourly Continuation — CKB/USDT P12_144

**Symbol:** CKB/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.6259 |
| net_win_rate | 0.4659 |
| gross_profit_factor | 0.9026 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -3.3979 |
| sortino_ratio | -1.0576 |
| max_drawdown | 0.7277 |
| cagr | -0.4029 |
| net_avg_win | 52.3586 |
| net_avg_loss | -72.9647 |
| avg_hold_time_bars | 30.3092 |
| exposure | 0.6861 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
