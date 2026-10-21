# EMA Hourly Continuation — XNO/USDT P12_144

**Symbol:** XNO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.7226 |
| net_win_rate | 0.4551 |
| gross_profit_factor | 0.8687 |
| gross_win_rate | 0.4551 |
| sharpe_ratio | -2.5404 |
| sortino_ratio | -0.7883 |
| max_drawdown | 0.6167 |
| cagr | -0.3045 |
| net_avg_win | 71.4791 |
| net_avg_loss | -82.6264 |
| avg_hold_time_bars | 27.3883 |
| exposure | 0.5963 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
