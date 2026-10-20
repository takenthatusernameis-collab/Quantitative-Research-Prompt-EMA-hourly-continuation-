# EMA Hourly Continuation — ALT/USDT P26_144

**Symbol:** ALT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.7102 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9316 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -2.3835 |
| sortino_ratio | -0.7468 |
| max_drawdown | 0.5982 |
| cagr | -0.2941 |
| net_avg_win | 60.7928 |
| net_avg_loss | -79.8272 |
| avg_hold_time_bars | 22.0739 |
| exposure | 0.4886 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
