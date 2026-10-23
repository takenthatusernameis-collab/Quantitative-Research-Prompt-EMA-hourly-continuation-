# EMA Hourly Continuation — ILV/USDT P55_144

**Symbol:** ILV/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.6829 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 0.9870 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -2.6874 |
| sortino_ratio | -0.8065 |
| max_drawdown | 0.6185 |
| cagr | -0.3177 |
| net_avg_win | 60.1459 |
| net_avg_loss | -84.2599 |
| avg_hold_time_bars | 12.8717 |
| exposure | 0.2645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
