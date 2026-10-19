# EMA Hourly Continuation — GRT/USDT P12_144

**Symbol:** GRT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.7154 |
| net_win_rate | 0.4933 |
| gross_profit_factor | 1.0019 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -2.4994 |
| sortino_ratio | -0.7422 |
| max_drawdown | 0.6351 |
| cagr | -0.2997 |
| net_avg_win | 67.7268 |
| net_avg_loss | -92.1625 |
| avg_hold_time_bars | 34.0919 |
| exposure | 0.6880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
