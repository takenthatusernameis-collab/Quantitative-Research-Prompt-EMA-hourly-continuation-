# EMA Hourly Continuation — W/USDT P12_144

**Symbol:** W/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.8949 |
| net_win_rate | 0.5431 |
| gross_profit_factor | 1.1913 |
| gross_win_rate | 0.5474 |
| sharpe_ratio | -0.6471 |
| sortino_ratio | -0.1992 |
| max_drawdown | 0.2898 |
| cagr | -0.0940 |
| net_avg_win | 74.2174 |
| net_avg_loss | -98.5766 |
| avg_hold_time_bars | 32.5819 |
| exposure | 0.6872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
