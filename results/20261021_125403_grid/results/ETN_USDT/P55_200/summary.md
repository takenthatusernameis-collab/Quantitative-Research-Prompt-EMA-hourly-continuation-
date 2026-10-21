# EMA Hourly Continuation — ETN/USDT P55_200

**Symbol:** ETN/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.5676 |
| net_win_rate | 0.4137 |
| gross_profit_factor | 0.6903 |
| gross_win_rate | 0.4137 |
| sharpe_ratio | -3.1411 |
| sortino_ratio | -0.8069 |
| max_drawdown | 0.5648 |
| cagr | -0.3116 |
| net_avg_win | 62.0775 |
| net_avg_loss | -77.1568 |
| avg_hold_time_bars | 19.3597 |
| exposure | 0.2923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
