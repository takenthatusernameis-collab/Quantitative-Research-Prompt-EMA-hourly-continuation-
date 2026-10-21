# EMA Hourly Continuation — EDU/USDT P12_89

**Symbol:** EDU/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.7850 |
| net_win_rate | 0.4961 |
| gross_profit_factor | 0.9615 |
| gross_win_rate | 0.4961 |
| sharpe_ratio | -1.7795 |
| sortino_ratio | -0.6437 |
| max_drawdown | 0.5496 |
| cagr | -0.2583 |
| net_avg_win | 60.5850 |
| net_avg_loss | -75.9898 |
| avg_hold_time_bars | 17.5272 |
| exposure | 0.5100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
