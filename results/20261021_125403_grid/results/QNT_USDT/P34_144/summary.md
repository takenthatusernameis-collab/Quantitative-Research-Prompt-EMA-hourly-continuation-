# EMA Hourly Continuation — QNT/USDT P34_144

**Symbol:** QNT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.7183 |
| net_win_rate | 0.4881 |
| gross_profit_factor | 0.9488 |
| gross_win_rate | 0.4881 |
| sharpe_ratio | -2.2232 |
| sortino_ratio | -0.6826 |
| max_drawdown | 0.5742 |
| cagr | -0.2684 |
| net_avg_win | 61.6360 |
| net_avg_loss | -81.8045 |
| avg_hold_time_bars | 16.1866 |
| exposure | 0.3392 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
