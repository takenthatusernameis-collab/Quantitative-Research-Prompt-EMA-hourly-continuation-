# EMA Hourly Continuation — MEW/USDT P26_89

**Symbol:** MEW/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.6786 |
| net_win_rate | 0.4650 |
| gross_profit_factor | 0.8355 |
| gross_win_rate | 0.4650 |
| sharpe_ratio | -2.4380 |
| sortino_ratio | -0.7525 |
| max_drawdown | 0.5880 |
| cagr | -0.2918 |
| net_avg_win | 55.8749 |
| net_avg_loss | -71.5570 |
| avg_hold_time_bars | 12.6624 |
| exposure | 0.2711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
