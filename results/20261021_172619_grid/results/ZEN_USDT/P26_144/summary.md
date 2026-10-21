# EMA Hourly Continuation — ZEN/USDT P26_144

**Symbol:** ZEN/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.7828 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9508 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -1.5126 |
| sortino_ratio | -0.4162 |
| max_drawdown | 0.4358 |
| cagr | -0.1758 |
| net_avg_win | 76.6110 |
| net_avg_loss | -92.7386 |
| avg_hold_time_bars | 27.8387 |
| exposure | 0.4707 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
