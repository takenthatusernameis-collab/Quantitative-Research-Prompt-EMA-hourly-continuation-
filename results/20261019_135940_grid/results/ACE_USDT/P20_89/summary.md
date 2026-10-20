# EMA Hourly Continuation — ACE/USDT P20_89

**Symbol:** ACE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 574 |
| net_profit_factor | 0.7341 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 1.0341 |
| gross_win_rate | 0.5087 |
| sharpe_ratio | -2.3027 |
| sortino_ratio | -0.7863 |
| max_drawdown | 0.6288 |
| cagr | -0.3034 |
| net_avg_win | 57.3373 |
| net_avg_loss | -78.6555 |
| avg_hold_time_bars | 15.7962 |
| exposure | 0.4103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
