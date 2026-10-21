# EMA Hourly Continuation — SNX/USDT P20_144

**Symbol:** SNX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.8989 |
| net_win_rate | 0.5222 |
| gross_profit_factor | 1.0902 |
| gross_win_rate | 0.5222 |
| sharpe_ratio | -0.6600 |
| sortino_ratio | -0.1911 |
| max_drawdown | 0.3163 |
| cagr | -0.0880 |
| net_avg_win | 87.0168 |
| net_avg_loss | -105.7834 |
| avg_hold_time_bars | 27.1897 |
| exposure | 0.4995 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
