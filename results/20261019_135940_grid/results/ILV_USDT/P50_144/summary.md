# EMA Hourly Continuation — ILV/USDT P50_144

**Symbol:** ILV/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.6866 |
| net_win_rate | 0.4923 |
| gross_profit_factor | 0.9854 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -2.6281 |
| sortino_ratio | -0.7939 |
| max_drawdown | 0.6162 |
| cagr | -0.3133 |
| net_avg_win | 59.4780 |
| net_avg_loss | -84.0150 |
| avg_hold_time_bars | 13.9650 |
| exposure | 0.2901 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
