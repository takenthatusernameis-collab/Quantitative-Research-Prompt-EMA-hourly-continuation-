# EMA Hourly Continuation — AMP/USDT P26_100

**Symbol:** AMP/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 935 |
| net_profit_factor | 0.3793 |
| net_win_rate | 0.3711 |
| gross_profit_factor | 0.6773 |
| gross_win_rate | 0.3872 |
| sharpe_ratio | -9.6950 |
| sortino_ratio | -4.1793 |
| max_drawdown | 0.9951 |
| cagr | -0.8756 |
| net_avg_win | 17.5156 |
| net_avg_loss | -27.2528 |
| avg_hold_time_bars | 8.8834 |
| exposure | 0.3775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
