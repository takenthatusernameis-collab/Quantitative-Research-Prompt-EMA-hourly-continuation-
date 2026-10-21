# EMA Hourly Continuation — ALT/USDT P12_144

**Symbol:** ALT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.7611 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9103 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -1.7158 |
| sortino_ratio | -0.4952 |
| max_drawdown | 0.4628 |
| cagr | -0.2049 |
| net_avg_win | 70.7841 |
| net_avg_loss | -85.6149 |
| avg_hold_time_bars | 34.9830 |
| exposure | 0.6535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
