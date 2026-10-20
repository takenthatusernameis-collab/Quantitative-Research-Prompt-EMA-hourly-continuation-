# EMA Hourly Continuation — CHR/USDT P8_89

**Symbol:** CHR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 710 |
| net_profit_factor | 0.6883 |
| net_win_rate | 0.4732 |
| gross_profit_factor | 0.9629 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -3.6059 |
| sortino_ratio | -1.3547 |
| max_drawdown | 0.8113 |
| cagr | -0.4711 |
| net_avg_win | 52.5515 |
| net_avg_loss | -68.5881 |
| avg_hold_time_bars | 20.3324 |
| exposure | 0.6532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
