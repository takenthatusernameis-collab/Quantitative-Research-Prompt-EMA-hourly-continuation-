# EMA Hourly Continuation — DCR/USDT P12_144

**Symbol:** DCR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.7800 |
| net_win_rate | 0.5048 |
| gross_profit_factor | 0.9929 |
| gross_win_rate | 0.5048 |
| sharpe_ratio | -1.5905 |
| sortino_ratio | -0.5188 |
| max_drawdown | 0.4866 |
| cagr | -0.2137 |
| net_avg_win | 61.0754 |
| net_avg_loss | -79.8112 |
| avg_hold_time_bars | 25.2314 |
| exposure | 0.5971 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
