# EMA Hourly Continuation — TAO/USDT P8_200

**Symbol:** TAO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 1.0748 |
| net_win_rate | 0.5515 |
| gross_profit_factor | 1.2174 |
| gross_win_rate | 0.5515 |
| sharpe_ratio | 0.4773 |
| sortino_ratio | 0.1205 |
| max_drawdown | 0.1443 |
| cagr | 0.0472 |
| net_avg_win | 106.3585 |
| net_avg_loss | -121.6827 |
| avg_hold_time_bars | 57.4884 |
| exposure | 0.7865 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
