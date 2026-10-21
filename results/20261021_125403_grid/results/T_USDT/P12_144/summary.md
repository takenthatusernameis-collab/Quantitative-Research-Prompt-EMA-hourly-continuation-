# EMA Hourly Continuation — T/USDT P12_144

**Symbol:** T/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.8926 |
| net_win_rate | 0.5343 |
| gross_profit_factor | 1.1473 |
| gross_win_rate | 0.5343 |
| sharpe_ratio | -0.6405 |
| sortino_ratio | -0.1683 |
| max_drawdown | 0.3256 |
| cagr | -0.0779 |
| net_avg_win | 85.8237 |
| net_avg_loss | -110.3302 |
| avg_hold_time_bars | 44.6866 |
| exposure | 0.6774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
