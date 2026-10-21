# EMA Hourly Continuation — XMR/USDT P12_144

**Symbol:** XMR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6774 |
| net_win_rate | 0.4635 |
| gross_profit_factor | 0.8734 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -2.6585 |
| sortino_ratio | -0.8159 |
| max_drawdown | 0.6429 |
| cagr | -0.3130 |
| net_avg_win | 59.3521 |
| net_avg_loss | -75.6987 |
| avg_hold_time_bars | 27.4185 |
| exposure | 0.5808 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
