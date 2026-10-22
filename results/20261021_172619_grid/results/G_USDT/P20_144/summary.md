# EMA Hourly Continuation — G/USDT P20_144

**Symbol:** G/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.5748 |
| net_win_rate | 0.4200 |
| gross_profit_factor | 0.7122 |
| gross_win_rate | 0.4200 |
| sharpe_ratio | -3.1341 |
| sortino_ratio | -0.8237 |
| max_drawdown | 0.6071 |
| cagr | -0.3165 |
| net_avg_win | 60.3293 |
| net_avg_loss | -76.0003 |
| avg_hold_time_bars | 37.9200 |
| exposure | 0.5982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
